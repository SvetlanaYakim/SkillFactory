# project 1. Analysis data HeadHunter

## Table of contents
[1. Project description](https://github.com/SvetlanaYakim/learn_skillfactory/blob/main/Project-1/readme.md#Project-description)

[2. What are we case solving?](https://github.com/SvetlanaYakim/learn_skillfactory/blob/main/Project-1/readme.md#What-are-we-case-solving)

[3. Bref information about the data](https://github.com/SvetlanaYakim/learn_skillfactory/blob/main/Project-1/readme.md#Bref-information-about-the-data)

[4. Stage of work on the project](https://github.com/SvetlanaYakim/learn_skillfactory/blob/main/Project-1/readme.md#Stage-of-work-on-the-project)

[5. Result](https://github.com/SvetlanaYakim/learn_skillfactory/blob/main/Project-1/readme.md#Result)

### Description of the project
Analysis of the resume database downloaded from the job search site hh.ru. 
link on the dataframe hh.ru (https://drive.google.com/file/d/1kRgpVhn7Ax22_1-tSB8fi2-QeNx9ACJQ/view?usp=sharing)
link on the dataframe with currency(https://drive.google.com/file/d/1XoDrI0XzZacDp6wN4U9j2wuY1A3GMZ-9/view?usp=sharing)

### What are we case solving?
Transform, explore and clean up the data.

### Bref information about the data
Our data is very "raw": the signs are presented in an inconvenient format for analysis and cleaning.
The data contains 12 features and 44744 rows.
features: Пол, возраст; ЗП; Ищет работу на должность:;
          Город, переезд, командировки; Занятость; График; Опыт работы;
          Последнее/нынешнее место работы; Последняя/нынешняя должность;
          Образование и ВУЗ; Обновление резюме; Авто.

### Stage of work on the project
Our project will consist of four parts:
- basic data structure analysis
    Let's get acquainted with the date frame how many columns and rows it contains. What format the data is in.

- data conversion
    'Образование и ВУЗ' attribute is presented in string format. We convert this attribute to the categories «высшее», «неоконченное высшее», «среднее специальное» and «среднее»

    'Пол, Возраст' attribute is presented in string format. let 's separate these signs. The gender attribute must have two unique string values: М — мужчина, Ж — женщина. 'Возраст' attribute must be represented by integers.

    'Опыт работы' attribute is presented in string format. Omissions and 'Не указано' are replaced with Nan. Converting values to months.

    'Город, переезд, командировки' attribute is presented in string format. Let's create separate signs 'Город', 'Готовность к переезду', 'Готовность к командировкам'. 'Город' attribute can contain only four categories: 'Москва', 'Санкт-Петербург' and 'город-миллионник' (their list in dataFrame), designate the rest as 'другие'. 'Готовность к переезду' sign should have two possible options: True or False. Признак 'Готовность к командировкам' sign should have two possible options: True or False.

    The signs 'Занятость' and 'График'. Now the signs represent a set of categories of desired employment (полная занятость, частичная занятость, проектная работа, волонтёрство, стажировка) and desired work schedule (полный день, сменный график, гибкий график, удалённая работа, вахтовый метод).
    let's create signs-"flashing lights" for each category: if the category is present in the list of desired by the applicant, then True is set in the column in place of the line of the applicant in question, otherwise False.

    'ЗП' is presented in different currencies. With the help of a dataframe with the exchange rate, we will convert the salary into rubles

- intelligence analysis
    Let's build graphs to identify abnormal values and dependencies.

- data cleanup
    Let's define duplicates and omissions. Delete those rows where there is a gap in the columns with the place of work and position, and fill in the gaps in the column with work experience with the median value. Let's determine the number of outliers by the z deviation method.

### Result
    The data contains 23 features and 44319 rows.
    features: Ищет работу на должность:; Последнее/нынешнее место работы;
            Последняя/нынешняя должность; Авто; Образование; Пол; Возраст;
            Опыт работы (месяц); Город; Готовность к переезду;
            Готовность к командировкам; полная занятость; частичная занятость;
            проектная работа; волонтерство; стажировка; полный день;
            сменный график; гибкий график; удалённая работа; вахтовый метод;
            date; ЗП (руб).
    As a result of the work, the data was transformed, we found anomalies in them: too much work experience, age 100 years. The category of education and the city with the highest salary were determined. We examined the dependence of average wages on age and education. Cleared the data from outliers.
    
:arrow_up:[To table of contents](https://github.com/SvetlanaYakim/learn_skillfactory/blob/main/project_0/readme.md#Project-description)