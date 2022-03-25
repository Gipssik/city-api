from pydantic import BaseModel


class NewYorkTimes(BaseModel):
    headline: str
    web_url: str
    lead_paragraph: str
    source: str
    pub_date: str
