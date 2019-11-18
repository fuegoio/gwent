import io from 'socket.io-client';

let sockets = {
    main: io('https://gwent-pooa.herokuapp.com/'),
    game: undefined
};

export default sockets
