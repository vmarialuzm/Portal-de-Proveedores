import axios from 'axios';

const usersApi = axios.create({
    baseURL: "http://127.0.0.1:8000/proveedores/",
});

export const createUser = (user) => usersApi.post('users/', user);

export const loginUser = (log) => usersApi.post('login/', log);