# app_calculator/middleware.py

class CORSMiddleware:
    """
    Middleware personalizado para adicionar cabeçalhos CORS às respostas HTTP.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Resposta padrão
        response = self.get_response(request)

        # Adiciona os cabeçalhos CORS
        response["Access-Control-Allow-Origin"] = "http://localhost:4200"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

        # Opcional: Permitir credenciais (cookies, autenticação)
        # response["Access-Control-Allow-Credentials"] = "true"

        # Se a solicitação for uma pré-verificação (preflight), retorna imediatamente
        if request.method == "OPTIONS":
            response.status_code = 200
            return response

        return response
