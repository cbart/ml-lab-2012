
let ilosc_probek = 1000
let nazwa_pliku = "example_file"
let max_x = 30.
let max_y = 30.

let kolo_fun x y =
  if (x-.15.)*.(x-.15.) +. (y-.15.)*.(y-.15.) < 100. then 1 else -1

let prosta_fun x y =
  if 3.*.x+.2.*.y-.5.>30. then 1 else -1

let prosta_random_fun x y =
  if x-.y>5. then 1 else
    if x-.y<(-5.) then -1 else 
      if Random.bool () then 1 else -1

let _ = 
  Random.self_init ();
  let file = open_out nazwa_pliku in
  for i = 1 to ilosc_probek do 
    let x = Random.float max_x in
    let y = Random.float max_y in
    let v = prosta_fun x y in
    Printf.fprintf file "%d 1:%f 2:%f\n" v x y
  done;
  close_out file