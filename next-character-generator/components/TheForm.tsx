import styles from "../styles/form.module.css"

interface TheFormProops {
    params: string[]
    change: any
    name: string
}

const TheForm: React.FC<TheFormProops> = ({ params , name, change}) => {
    return (
        <select className={styles.form} name={name} onChange={change}>
            {params.map((param, index) => (
                <option className={styles.item} key={index} value={param}>{param}</option>
                ))
            }
        </select>
    );
};

export default TheForm;