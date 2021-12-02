(with [f (open "day02/input")]
    (setv commands (list (map str.split (.readlines f)))))

(defn traverse [extended]
    (setv x 0
          y 0
          aim 0)
    (defn vertical-accumulator [v]
        (nonlocal y aim)
        (cond [extended (+= aim v)]
              [(not extended) (+= y v)]))
    (list (map
        (fn [tup]
            (nonlocal x y)
            (setv cmd (get tup 0)
                  units (int (get tup 1)))
            (cond
                [(= cmd "forward")
                 (+= x units)
                 (if extended (+= y (* aim units)))]
                [(= cmd "up")
                 (vertical-accumulator (- units))]
                [(= cmd "down")
                 (vertical-accumulator units)]))
        commands))
    (print (* x y)))

(traverse False)
(traverse True)
