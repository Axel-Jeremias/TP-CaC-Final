export const ListPages = {
    data: function() {
        return {
            pages: [
                {
                    nombre: "index",
                    titulo: "Inicio"
                },
                {
                    nombre: "cartelera",
                    titulo: "Cartelera"
                },
                {
                    nombre: "servicios",
                    titulo: "Preguntas frecuentes"
                },
                {
                    nombre: "contacto",
                    titulo: "Contacto"
                }
            ]
        }
    },
    template: `
        <li v-for="page in pages">
            <a :href="page.nombre">{{ page.titulo }}</a>
        </li>
    `,
};