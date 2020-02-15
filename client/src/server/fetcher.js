import axios from 'axios';

const fetcher = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    withCredentials: true,
});

export default fetcher;

// 'http://localhost:5000'