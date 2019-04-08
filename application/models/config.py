import web

db_host = 'bmsyhziszmhf61g1.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'emu896o5x5926xvn'
db_user = 'dzlmadj8085s2x4i'
db_pw = 'jg1j0yzbm7s82def'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
