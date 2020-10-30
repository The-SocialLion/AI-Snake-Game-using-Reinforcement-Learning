from snake.game import Game, GameConf, GameMode

greedy = "GreedySolver"
hamilton = "HamiltonSolver"
dqn= "deep qnetwork"
normal = GameMode.NORMAL


conf = GameConf()
conf.solver_name = dqn
conf.mode = normal
print("Solver: %s " % (conf.solver_name))
print("Mode: %s" %(conf.mode))
Game(conf).run()
