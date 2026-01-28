from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Address:
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Dict[str, Any]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Address":
        return Address(
            street=data.get("street", ""),
            suite=data.get("suite", ""),
            city=data.get("city", ""),
            zipcode=data.get("zipcode", ""),
            geo=data.get("geo", {}),
        )


@dataclass
class Company:
    name: str
    catchPhrase: str
    bs: str

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Company":
        return Company(
            name=data.get("name", ""),
            catchPhrase=data.get("catchPhrase", ""),
            bs=data.get("bs", ""),
        )


@dataclass
class User:
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "User":
        return User(
            id=data["id"],
            name=data["name"],
            username=data["username"],
            email=data["email"],
            address=Address.from_dict(data["address"]),
            phone=data["phone"],
            website=data["website"],
            company=Company.from_dict(data["company"]),
        )