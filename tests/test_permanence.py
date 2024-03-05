import json

from perm.model.permanence import Permanence, PermanenceJsonEncoder

BASIC_PERM = Permanence(title="mytitle", datestr="10/05/2025", startstr="14h",
                        endstr="18h", description="mydescription")
BASIC_PERM.validate()


def test_perm_json() -> None:
    basic_list = list()
    basic_list.append(BASIC_PERM)
    print(json.dumps(basic_list, cls=PermanenceJsonEncoder))
