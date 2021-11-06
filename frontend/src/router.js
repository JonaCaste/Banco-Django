import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App'

import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'

const routes = [
  {
    path: '/',
    name: 'root',     //el nombre redirecciona al path
    component: App
  },
  {
    path:'/user/login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path:'/user/SignUp',
    name: 'SignUp',
    component: SignUp
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
