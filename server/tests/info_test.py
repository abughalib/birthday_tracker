from ..utils import validator
from ..constants import COMPANY_DOMAIN


def test_personal_email():
    pm = ["abc@sdafshadkf.com", "adsihfoiewhw@asdof.com", "isdafj.com", "@@.com"]

    pmv = [True, True, False, False]

    for i in range(len(pm)):
        assert validator.verify_email(pm[i]) == pmv[i]


def test_work_email():
    wm = [
        f"abc@{COMPANY_DOMAIN}",
        f"dsjafsfaf@{COMPANY_DOMAIN}",
        "asdfiojdsaoi;@fasdjfl.com",
        f"fewji.213aof@{COMPANY_DOMAIN}",
        f"@{COMPANY_DOMAIN}",
        "asdfjioew@dasjffld.com",
        "asfjioewjfe@adf.",
    ]

    wm_exp = [True, True, False, True, False, False, False]

    for i in range(len(wm)):
        assert validator.verify_email(wm[i], True) == wm_exp[i]


def test_phone():
    pn = [
        "sdfljsdafu",
        "9097712750",
        "8808324324",
        "432432432434",
        "973209473209473209",
        "343243244",
        "3243fdf34r",
    ]

    pv = [False, True, True, False, False, False, False]

    for i in range(len(pn)):
        assert validator.verify_phone(pn[i]) == pv[i]


if __name__ == "__main__":
    test_personal_email()
    test_work_email()
    test_phone()
