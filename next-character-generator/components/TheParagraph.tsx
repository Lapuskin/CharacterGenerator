import styles from "../styles/paragraph.module.css"

interface TheParagraphProps {
  title: string;
  text1: string;
  text2: string;
  text3: string;
}

const TheParagraph: React.FC<TheParagraphProps> = ({ title, text1,text2, text3 }) => {
  return (
    <div className={styles.paragraph}>
      <div className={styles.title}>
        <img src="vector_left.svg" alt="левая угасающая векторная линия" />
        <img src="star.svg" alt="иконка четырехконечной звезды" />
        <h1>{title}</h1>
        <img src="star.svg" alt="иконка четырехконечной звезды" />
        <img src="vector_right.svg" alt="правая угасающая векторная линия" />
      </div>
      <p className={styles.text}>{text1}</p>
      <p className={styles.text}>{text2}</p>
      <p className={styles.text}>{text3}</p>
      <img src="line.svg" alt="прямая, отделяющая контент" />
    </div>
  );
};

export default TheParagraph;
