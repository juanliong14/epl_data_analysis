import epl_data_scraping as epl_ds

match_id_20_21 = list(range(58896,59276))
match_id_19_20 = list(range(46605,46985))
match_id_18_19 = list(range(38308,38688))

match_id = []
match_id += match_id_18_19 
match_id += match_id_19_20
match_id += match_id_20_21 

epl_ds.get_data(match_id=match_id,file_name='epl_data_complete')