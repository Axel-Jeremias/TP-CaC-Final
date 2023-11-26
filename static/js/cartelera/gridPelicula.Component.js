export const GridPeliculas = {
    template: `
        <div id="peliculasGrid">
            <div v-for="pelicula in peliculas" class="peli">
                <img :src="pelicula.poster_path" :alt="'Portada de la pelicula ' + pelicula.title">
                <div class="dataPeli">
                    <div class="titulo">
                        <h6 :title="pelicula.title">{{ pelicula.title }}</h6>
                    </div>
                    <ul>
                        <li title="Calificación">
                            <i class="fa-solid fa-star" style="color: #fdd649;"></i>
                            <span>{{ pelicula.rating }}</span>
                        </li>
                        <li title="Fecha de lanzamiento">
                            <i class="fa-regular fa-calendar" style="color: #ffffff;"></i>
                            <span>{{ pelicula.fecha }}</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    `,
    props: {
        peliculas: Array
    }
};