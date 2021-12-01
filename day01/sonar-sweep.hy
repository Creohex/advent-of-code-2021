
(with [f (open "day01/input")]
    (setv sequence (list (map int (.readlines f)))))

(defn count-increases [seq]
    (print (len (list (filter
        (fn [pair] (> (get pair 1) (get pair 0)))
        (zip seq (cut seq 1 (len seq))))))))

(count-increases sequence)
(count-increases (list (map sum (zip
    sequence
    (cut sequence 1 (len sequence))
    (cut sequence 2 (len sequence))))))
