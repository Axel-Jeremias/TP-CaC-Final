export const Novedad = {
    template: `
        <div id="slide">
            <h3 id="titulo">{{ nuevaNovedad.titulo }}</h3>

            <div id="info-slide">
                <h3>{{ nuevaNovedad.titulo }}</h3>
                <p>{{ nuevaNovedad.descripcion }}</p>
            </div>

            <div id="image-container">
                <img id="slide-image" :src="'/static/img/novedades/' + nuevaNovedad.url" :alt="nuevaNovedad.titulo">
            </div>
        </div>
    `,
    props: {
        nuevaNovedad: Object,
    },
};