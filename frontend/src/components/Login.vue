<template>
    <div class="logInUser">
        <div class="container">
            <h2>Iniciar sesión</h2>
            <form v-on:submit.prevent="processLoginUser">
                <input type="text" placeholder="UserName" v-model="user.username">
                <!-- v-model -> asocia a un modelo "interno", "se crea el objeto JSON que se envia el la peticion" 
                    que espera el backend -->
                <!-- este input guarda username del modelo user -->
                <br>
                <input type="password" placeholder="Contraseña" v-model="user.password">
                <br>
                <button type="submit">Iniciar sesión</button>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name : 'LogIn',

        data : function(){
            return{
                user : {
                    username : "",
                    password : "",
                }
            }
        },

        methods : {
            processLoginUser: function(){
                axios.post(
                    "http://127.0.0.1:8000/login/",                     //endpoint
                    this.user,                                          //lo que enviamos
                    {headers:{}}                                        //headers vacios, ya que el back no necesita
                )                                                       //peticion post
                .then(result => {
                    let dataLogin = {
                        username : this.user.username,                  //username del objeto user
                        token_access : result.data.access,              //token de la data de respuesta
                        token_refresh : result.data.refresh             //token de la data de respuesta
                    };

                    this.$emit('completedLogIn', dataLogin);              //enviamos info a la app padre, y ejecuta esa funcion
                })
                .catch(error => {
                    if(error.response.status == "401"){
                        alert("Las credenciales son incorrectas");
                    }
                })
            }
        }
    }
</script>

<style>
    .logIn_user{
        margin: 0;
        padding: 0;
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_logIn_user{
        border: 3px solid #283747;
        border-radius: 10px;
        width: 25%;
        height: 60%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .logIn_user h2{
        color: #283747;
    }

    .logIn_user form{
        width: 70%;
    }

    .logIn_user input{
        height: 40px;
        width: 100%;
        padding: 10px 20px;
        margin: 5px 0;
        border: 1px solid #e5e7e9;
    }

    .logIn_user button{
        width: 100%;
        height: 40px;
        color: #e5e7e9;
        background: #283747;
        border: 1px solid #e5e7e9;
        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0;
    }

    .logIn_user button:hover{
        color: #283747;
        background: #e5e7e9;
        border: 1px solid #283747;
    }
</style>