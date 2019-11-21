import io from 'socket.io-client';

let sockets = {
    main: io(process.env.VUE_APP_API_URL),
    game: undefined
};

export default sockets
