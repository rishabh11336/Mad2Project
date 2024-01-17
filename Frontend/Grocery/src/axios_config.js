// axios.js

import axios from 'axios'

const instance = axios.create({
  baseURL: 'http://127.0.0.1:5000'
  //    Other Axios configuration options if needed
})

// Add an interceptor to include the authorization header
instance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

export default instance