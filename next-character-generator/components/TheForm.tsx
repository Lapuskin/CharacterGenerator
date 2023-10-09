import Link from "next/link";
import styles from "../styles/form.module.css"

interface TheFormProops {
    params: string[];
}

const TheForm: React.FC<TheFormProops> = ({ params }) => {
    return (
        <div className={styles.form}>
            {params.map((param, index) => (
                <option key={index} value={param}>{param}</option>
            ))
                }
        </div>
    );
};

export default TheForm;