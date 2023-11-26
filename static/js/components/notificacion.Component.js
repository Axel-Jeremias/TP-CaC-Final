export const Notificacion = {
    props: {
        enviado: Boolean,
    },
    data: function() {
        return {
            icono: `fa-solid ${this.enviado ? "fa-check" : "fa-xmark"}`,
            tipoNotificacion: `notificacion ${this.enviado ? "exito" : "fallo"}`,
            texto: this.enviado ? "Formulario enviado con exito" : "Formulario no enviado"
        }
    },
    template: `
        <div :class="tipoNotificacion">
            <i :class="icono"></i>
            <span>{{ texto }}</span>
        </div>
    `
};