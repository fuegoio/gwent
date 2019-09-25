from __future__ import annotations

from gwent import create_app, create_game

app = create_app()

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000, debug=True)
    game = create_game('Fuego', 'Moulq')
    game.run()
