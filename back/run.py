import uvicorn

from gwent import create_app, create_game

app = create_app()

if __name__ == '__main__':
    game = create_game('Fuego', 'Moulq')
    game.run()

    uvicorn.run(app, host="0.0.0.0", port=3000)

