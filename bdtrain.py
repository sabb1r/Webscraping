class Train:
    instance = []

    def __init__(self, name, code, off_day, stations, exclude_stations=None, include_stations=None):
        self.__class__.instance.append(self)
        self.name = name
        self.code = code
        self.odd_stations = stations
        self.off_day = off_day
        self.exclude_stations = exclude_stations

        if not exclude_stations:
            self.even_stations = stations[::-1]
        else:
            self.even_stations = [station for station in stations[::-1] if station not in exclude_stations]

        if include_stations:
            for station, ind in include_stations:
                self.even_stations.insert(ind, station)

    def previous_stations(self, code, station):
        if self.odd_stations[0] == station or self.even_stations[0] == station:
            return None
        return self.odd_stations[:self.odd_stations.index(station)] if code % 2 == 1 else self.even_stations[:self.even_stations.index(station)]

    def next_stations(self, code, station):
        if self.odd_stations[-1] == station or self.even_stations[-1] == station:
            return None
        return self.odd_stations[self.odd_stations.index(station)+1:] if code % 2 == 1 else self.even_stations[self.even_stations.index(station)+1:]

    def remaining_stations(self, code, station):
        return


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

drutojan_757_stations = ['Dhaka', 'Biman_Bandar', 'Joydebpur', 'Tangail', 'BBSetu_E', 'Jamtail', 'Chatmohar', 'Natore',
                         'Ahsanganj', 'Santahar', 'Akkelpur', 'Joypurhat', 'Panchbibi', 'Birampur', 'Fulbari',
                         'Parbatipur', 'Chirirbandar', 'Dinajpur', 'Setabganj', 'Pirganj', 'Thakurgaon_Road', 'Ruhia',
                         'Kismat', 'B Sirajul Islam']
drutojan_exclude_stations = ['Biman_Bandar']
drutojan_include_stations = [('Ishwardi Bypass', 17)]

chilahati_805_stations = ['Dhaka', 'Biman_Bandar', 'Joydebpur', 'Ishwardi Bypass', 'Natore', 'Santahar', 'Joypurhat',
                          'Birampur', 'Fulbari', 'Parbatipur', 'Saidpur', 'Nilphamari', 'Domar', 'Chilahati']
chilahati_exclude_stations = ['Biman_Bandar']

Banalata = Train('BANALATA EXPRESS', 791, 'Friday', banalata_791_stations, banalata_exclude_stations)
Silkcity = Train('SILKCITY EXPRESS', 753, 'Sunday', silkcity_753_stations, silkcity_exclude_stations)
Padma = Train('PADMA EXPRESS', 759, 'Tuesday', padma_759_stations, padma_exclude_stations)
Dhumketu = Train('DHUMKETU EXPRESS', 769, 'Wednesday', dhumketu_769_stations, dhumketu_exclude_stations)
Ekota = Train('EKOTA EXPRESS', 705, None, ekota_705_stations, ekota_exclude_stations)
Drutojan = Train('DRUTOJAN EXPRESS', 757, None, drutojan_757_stations, drutojan_exclude_stations,
                 drutojan_include_stations)
Chilahati = Train('CHILAHATI EXPRESS', 805, 'Saturday', chilahati_805_stations, chilahati_exclude_stations)


trains = [Banalata, Silkcity, Padma, Dhumketu, Ekota, Drutojan, Chilahati]

import pickle
with open('train_database.pkl', 'wb') as f:
    pickle.dump(trains, f)