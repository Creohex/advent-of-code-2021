(import numpy)

(setv crabs (numpy.array (list (map int (str.split (.read (open "day07/input")) ",")))))
(defn count-fuel [target incremental]
    (print (sum (map
        (fn [crab] (cond [(not incremental) (abs (- crab target))]
                         [incremental (sum (range 1 (+ (abs (- crab target)) 1)))]))
        crabs))))

(count-fuel (int (numpy.median crabs)) False)
(count-fuel (int (.mean crabs)) True)
