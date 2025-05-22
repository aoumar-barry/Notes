from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    path = request.url.path
    error_messages = []

    for error in exc.errors():
        field = error.get("loc")[-1]
        error_type = error.get("type")
        ctx = error.get("ctx", {})

        # 🔀 Route-specific translation
        if path == "/register/":
            if error_type == "value_error.missing":
                error_messages.append(f"Le champ {field} est requis.")
            elif error_type == "value_error.any_str.min_length":
                error_messages.append(f"Le champ {field} doit contenir au moins {ctx.get('limit_value')} caractères.")
            elif error_type == "value_error.email":
                error_messages.append(f"Le champ {field} doit être une adresse email valide.")
            else:
                error_messages.append(f"Erreur sur le champ {field}.")
        
        elif path == "/order/":
            if error_type == "value_error.missing":
                error_messages.append(f"Le champ {field} de la commande est requis.")
            elif error_type == "type_error.integer":
                error_messages.append(f"Le champ {field} doit être un nombre entier.")
            elif error_type == "value_error.number.not_ge":
                error_messages.append(f"Le champ {field} doit être supérieur ou égal à {ctx.get('limit_value')}.")
            else:
                error_messages.append(f"Erreur dans la commande sur le champ {field}.")
    
    return JSONResponse(status_code=422, content=error_messages)
