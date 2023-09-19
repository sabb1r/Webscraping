class Train:
    def __init__(self, name, code, off_day, stations, exclude_stations=None):
        self.name = name
        self.code = code
        self.odd_stations = stations
        self.off_day = off_day
        self.exclude_stations = exclude_stations

        if not exclude_stations:
            self.even_stations = stations[::-1]
        else:
            self.even_stations = [station for station in stations[::-1] if station not in exclude_stations]

    def previous_stations(self, code, station):
        return self.odd_stations[:self.odd_stations.index(station)] if code%2 == 1 else self.even_stations[:self.even_stations.index(station)]


banalata_791_stations = ['Dhaka', 'Biman_Bandar', 'Rajshahi', 'Chapai Nawabganj']
banalata_exclude_stations = ['Biman_Bandar']

silkcity_753_stations = ['Dhaka', 'Biman_Bandar', 'Joydebpur', 'Mirzapur', 'Tangail', 'BBSetu_E', 'SH M Monsur Ali',
                         'Jamtail', 'Ullapara', 'Boral_Bridge', 'Chatmohar', 'Ishwardi Bypass', 'Abdulpur', 'Rajshahi']
silkcity_exclude_stations = ['Biman_Bandar']

padma_759_stations = ['Dhaka', 'Biman_Bandar', 'Joydebpur', 'Tangail', 'BBSetu_E', 'SH M Monsur Ali', 'Ullapara',
                      'Boral_Bridge', 'Chatmohar', 'Ishwardi Bypass', 'Abdulpur', 'Sardah_Road', 'Rajshahi']
padma_exclude_stations = ['Biman_Bandar']

dhumketu_769_stations = ['Dhaka', 'Biman_Bandar', 'Joydebpur', 'Tangail', 'BBSetu_E', 'SH M Monsur Ali', 'Jamtail',
                         'Ullapara', 'Boral_Bridge', 'Chatmohar', 'Ishwardi Bypass', 'Abdulpur', 'Arani', 'Rajshahi']
dhumketu_exclude_stations = ['Biman_Bandar', 'Tangail', 'Jamtail', 'Ullapara', 'Ishwardi Bypass']

ekota_705_stations = ['Dhaka', 'Biman_Bandar', 'Joydebpur', 'Tangail', 'BBSetu_E', 'SH M Monsur Ali', 'Ullapara',
                      'Ishwardi Bypass', 'Natore', 'Santahar', 'Akkelpur', 'Joypurhat', 'Panchbibi', 'Birampur',
                      'Fulbari', 'Parbatipur', 'Chirirbandar', 'Dinajpur', 'Setabganj', 'Pirganj', 'Thakurgaon_Road',
                      'Ruhia', 'Kismat', 'B Sirajul Islam']
ekota_exclude_stations = ['Biman_Bandar', 'SH M Monsur Ali', 'Ishwardi Bypass']


Banalata = Train('BANALATA EXPRESS', 791, 'Friday', banalata_791_stations, banalata_exclude_stations)
Silkcity = Train('SILKCITY EXPRESS', 753, 'Sunday', silkcity_753_stations, silkcity_exclude_stations)
Padma = Train('PADMA EXPRESS', 759, 'Tuesday', padma_759_stations, padma_exclude_stations)
Dhumketu = Train('DHUMKETU EXPRESS', 769, 'Wednesday', dhumketu_769_stations, dhumketu_exclude_stations)
Ekota = Train('EKOTA EXPRESS', 705, None, ekota_705_stations, ekota_exclude_stations)

