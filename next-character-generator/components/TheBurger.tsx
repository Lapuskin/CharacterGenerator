'use client'
import styles from "../styles/burger.module.css"


interface TheBurgerProps {
    open: boolean;
    setOpen: any;
}

const TheBurger: React.FC<TheBurgerProps> = ({ open, setOpen }) => {
    return (
            <div className={styles.icon} onClick={() => setOpen(!open)}>
                <hr />
                <hr />
                <hr />
            </div>
    );
};

export default TheBurger;