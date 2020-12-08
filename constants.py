DO_DOWNLOAD=False

DAY_IN_NS = int(864e11)

URLs = {
    'BAG_test_data': 'https://www.bag.admin.ch/dam/bag/de/dokumente/mt/k-und-i/aktuelle-ausbrueche-pandemien/2019-nCoV/covid-19-basisdaten-labortests.xlsx.download.xlsx/Dashboard_3_COVID19_labtests_positivity.xlsx',
    'BAG_report_data': 'https://www.bag.admin.ch/dam/bag/de/dokumente/mt/k-und-i/aktuelle-ausbrueche-pandemien/2019-nCoV/covid-19-datengrundlage-lagebericht.xlsx.download.xlsx/200325_Datengrundlage_Grafiken_COVID-19-Bericht.xlsx'
}

FOLDERS = {
    'BAG_data': 'data/bag/',
    'openZH_data': 'data/openZH/'
}

FIGURE_TEMPLATE = 'simple_white'

CANTONS = {
    "01": "AK",
    "02": "AL",
    "03": "AR",
    "04": "AZ",
    "05": "CA",
    "06": "CO",
    "07": "CT",
    "08": "DC",
    "09": "DE",
    "10": "FL",
    "11": "GA",
    "12": "HI",
    "13": "IA",
    "14": "ID",
    "15": "IL",
    "16": "IN",
    "17": "KS",
    "18" : "KY",
    "19" : "LA",
    "20" : "MA",
    "21" : "MD",
    "22" : "ME",
    "23" : "MI",
    "24" : "MN",
    "25" : "MO",
    "26" : "MS",
    "27" : "MT",
    "28" : "NC",
    "29" : "ND",
    "30" : "NE",
    "31" : "NH",
    "32" : "NJ",
    "33" : "NM",
    "34" : "NV",
    "35" : "NY",
    "36" : "OH",
    "37" : "OK",
    "38" : "OR",
    "39" : "PA",
    "40" : "RI",
    "41" : "SC",
    "42" : "SD",
    "43" : "TN",
    "44" : "TX",
    "45" : "UT",
    "46" : "VA",
    "47" : "VT",
    "48" : "WA",
    "49" : "WI",
    "50" : "WV",
    "51" : "WY"
}
