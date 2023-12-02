import { Notificacion } from '../components/notificacion.Component.js';

export const contactoCore = {
    data: function() {
        return {
            mostrarNotificacion: false,
            enviado: false,
            sheetURL: "https://sheetdb.io/api/v1/jwo0kp5sv91ao?mode=RAW"
        }
    },
    components: {
        Notificacion: Notificacion,
    },
    methods: {
        validarFormulario: async function(event) {
            const valores = new FormData(event.target);
            const formulario = Object.fromEntries(valores);
        
            if (formulario.comentario.length <= 10) {
                alert("Por favor, incluya un comentario (minimo 10 caracteres)");
            } else if (/\d/.test(formulario.nombre) || /\d/.test(formulario.apellido)) {
                alert("Por favor, incluya un nombre y apellido validos.");
            } else {            
                await this.enviarFormulario(valores);
                document.contactoForm.reset();
                this.enviado = true;
            }

            this.mostrarNotificacion = true;

            setTimeout(() => {
                this.mostrarNotificacion = false;
            }, 8000);
        },
        enviarFormulario: async function(formulario) {
            formulario.append("fechaCreacion", "DATETIME");
            formulario.append("NumeroTicket", "INCREMENT");
        
            const configuracion = {
                method: "POST",
                body: formulario,
            };
        
            await fetch(this.sheetURL, configuracion);
        }
    }
};