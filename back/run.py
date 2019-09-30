import uvicorn

from gwent import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3000)

    # game = create_game('Fuego', 'Moulq')
    # game.run()
