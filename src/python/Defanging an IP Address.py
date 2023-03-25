"""
Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:

    The given address is a valid IPv4 address.

"""


class Solution:
    def defangIPaddr(self, address: str) -> str:  # IDK what's wrong with LC's memory counter LOL
        address = address.replace(".", "[.]")
        return address

    def defangIPaddr4(self, address: str) -> str:
        address = list(address)
        for i in range(len(address)):
            if address[i] == ".":
                address[i] = "[.]"
        return "".join(address)

    def defangIPaddr3(self, address: str) -> str:
        return "".join([i if i != "." else "[.]" for i in address])

    def defangIPaddr2(self, address: str) -> str:
        return "[.]".join(address.split("."))

    def defangIPaddr1(self, address: str) -> str:
        return address.replace(".", "[.]")
