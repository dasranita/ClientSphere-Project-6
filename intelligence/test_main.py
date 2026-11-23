from main import score,Lead,forecast,Opportunity
def test_score():assert score(Lead(name='A',engaged=True))['score']==35
def test_forecast():assert forecast([Opportunity(amount=100,probability=.5)])['weighted_forecast']==50
