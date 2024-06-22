from enum import Enum
from dataclasses import dataclass
from datetime import date


class CicloContagem(str, Enum):
    TRI     = "Tri-horário"
    BI      = "Bi-horário"
    SIMPLES = "Simples"


class CicloPeriodo(str, Enum):
    DAILY  = "Diário"
    WEEKLY = "Semanal"


@dataclass
class TarifaTipo:
    FIXA     = "Fixa"
    VARIAVEL = "Variável"


@dataclass
class TarifaCiclo:
    ponta: float
    fora_vazio: float
    vazio: float
    flat: float


class TarifaPotencia:
    potencia_minima: float
    potencia_maxima: float
    custo_minuto: float
    custo_kwh: float


@dataclass
class TarifaCEME:

    nome: str
    condicionantes: str
    url: str
    data_atualizacao: str
    data_inicio: date
    data_fim: date
    historica: bool  
    energia_verde: bool
    pagamento_app: bool
    pagamento_rfid: bool

    tipo_tarifa: TarifaTipo
    ciclo_contagem: CicloContagem
    ciclo_periodo: CicloPeriodo
    inclui_egme: bool
    inclui_tar: bool
    inclui_iec: bool
    inclui_iva: bool
    inclui_opc: bool
    taxa_ativacao: float

    custo_potencia: None | list[TarifaPotencia]
    custo_minuto: TarifaCiclo
    custo_kwh: TarifaCiclo



