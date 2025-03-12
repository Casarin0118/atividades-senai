from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import re

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


def validate_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digit(digits):
        sum_ = sum(int(d) * w for d, w in zip(digits, range(len(digits) + 1, 1, -1)))
        digit = (sum_ * 10 % 11) % 10
        return str(digit)

    return cpf[-2:] == calc_digit(cpf[:9]) + calc_digit(cpf[:10])


@app.get("/validate")
def validate(cpf: str):
    is_valid = validate_cpf(cpf)
    return JSONResponse(content={"cpf": cpf, "valid": is_valid})
