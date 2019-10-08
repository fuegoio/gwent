import io from 'socket.io-client';

let sockets = {
    main: io('http://localhost:3000/'),
    game: undefined
};

export default sockets
