# Порівняння алгоритмів сортування: Merge Sort, Insertion Sort, Timsort

## Опис завдання

Мета: порівняти три алгоритми сортування: **злиттям (Merge Sort)**, **вставками (Insertion Sort)** та **Timsort** (стандартний вбудований у Python), замірявши їх час виконання на різних розмірах вхідних даних. Для тестування використовувався модуль `timeit`.

## Теоретична складність

| Алгоритм        | Середня складність | Найгірший випадок | Найкращий випадок |
|-----------------|-------------------|------------------|-------------------|
| Merge Sort      | O(n log n)        | O(n log n)       | O(n log n)        |
| Insertion Sort  | O(n^2)            | O(n^2)           | O(n)              |
| Timsort (sorted)| O(n log n)        | O(n log n)       | O(n)              |

## Емпіричні результати

| Size   | Merge Sort | Insertion Sort | Timsort (sorted) |
|--------|------------|---------------|------------------|
|   100  | 0.000073s  | 0.000076s     | 0.000006s        |
|  1000  | 0.000765s  | 0.008192s     | 0.000068s        |
|  5000  | 0.004331s  |      nan      | 0.000369s        |
| 10000  | 0.008873s  |      nan      | 0.000753s        |

> **Примітка:** для великих розмірів масивів (`Insertion Sort`) виникли проблеми з вимірюванням часу через надто довге виконання, що відображено як `nan`.

## Висновки

- **Timsort (`sorted`)** - найшвидший з протестованих алгоритмів на всіх розмірах масиву. Це пояснюється його гібридною природою (поєднання сортування злиттям та вставками) та численними оптимізаціями для різних типів даних.  
  У реальних задачах рекомендується використовувати саме вбудовану функцію `sorted` або метод `.sort()`.

- **Merge Sort** - показав передбачувану ефективність (O(n log n)), добре масштабується зі збільшенням розміру масиву. Хоча повільніший за Timsort, значно ефективніший за прості алгоритми на великих наборах даних.

- **Insertion Sort** - алгоритм, чий час різко зростає зі збільшенням кількості елементів (O(n^2)). Для великих масивів не підходить, оскільки працює дуже повільно. Може бути корисний лише для дуже малих або майже відсортованих масивів.
