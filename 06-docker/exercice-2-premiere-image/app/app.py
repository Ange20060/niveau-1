import time
from flask import Flask, request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# 1. Définition des métriques (les capteurs)
REQUEST_COUNT = Counter(
    'app_requests_total', 
    'Nombre total de requêtes HTTP reçues',
    ['method', 'endpoint', 'http_status'] # Permet de filtrer par méthode, URL et code HTTP
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds', 
    'Duree des requetes HTTP en secondes',
    ['method', 'endpoint']
)

# 2. Enregistrement automatique du temps et du compteur avant/après chaque requête
@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def record_metrics(response):
    # On calcule le temps que la requête a pris
    diff = time.time() - request.start_time
    
    # On enregistre les données dans Prometheus
    REQUEST_LATENCY.labels(request.method, request.path).observe(diff)
    REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
    
    return response

# Tes routes d'origine
@app.route("/")
@app.route("/api")
def hello():
    return "Hello depuis mon conteneur Docker !\n"

# 3. Le endpoint /metrics requis par l'exercice
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    # 0.0.0.0 pour que l'appli soit joignable depuis l'extérieur du conteneur
    app.run(host="0.0.0.0", port=5000)
 