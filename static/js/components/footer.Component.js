import { ListPages } from "./listPages.Component.js";

export const Footer = {
    components: {
        ListPages: ListPages
    },
    template: `
        <footer>
            <ul id="lista-footer">
                <ListPages></ListPages>
            </ul>
        </footer>
    `,
};