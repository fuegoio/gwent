import io from 'socket.io-client';

let sockets = {
    main: io('http://gwent-pooa.herokuapp.com/'),
    game: undefined
};

export default sockets
