import styles from "../styles/button.module.css"

interface TheButtonProops {
    text: string;
}

const TheButton: React.FC<TheButtonProops> = ({ text }) => {
    return (<div className={styles.block}>
            <button className={styles.button} type='submit'>{text}</button>
            </div>
    );
};

export default TheButton;