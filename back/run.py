import os

import uvicorn

from gwent import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get('PORT', 3000)))

