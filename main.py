from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithID
app = FastAPI()

BANDS = [
    {
        'id':1, 'name':'The Kinks', 'genre': 'Rock'
    },
    {
        'id':2, 'name':'The ship', 'genre': 'Fight', 'albums':[{
            'title':'Master of reality', 'release_date':'1971-07-21'
        }]
    },
    {
        'id':3, 'name':'RED', 'genre': 'suspense'
    },
    {
        'id':4, 'name':'Avenger', 'genre':'action'
    },
]

@app.get('/bands')
async def bands()->list[BandWithID]:
    return [BandWithID(**b) for b in BANDS]

@app.get('/bands/{band_id}') 
async def band(band_id:int) -> BandWithID:
    band = next((BandWithID(**b) for b in BANDS if b['id'] ==  band_id), None)
    if band is None:
        raise HTTPException(status_code = 404, detail='band not found')
    return band

@app.post('/bands')
async def create_band(band_data: BandCreate) -> BandWithID:
    id = BANDS[-1]['id'] + 1
    band = BandWithID(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band





