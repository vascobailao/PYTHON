import gym
import numpy as np

env = gym.make('FrozenLake-v0')


# Formula Q-Learning: Q[s,a]= Q'[s,a] + alpha*(reward + gamma* max(Q[s(t+1),a]) - Q'[s,a])


# Tabela inicial estado x acao
Q = np.zeros([env.observation_space.n,env.action_space.n])


# variaveis auxiliares
alpha = .85
gamma = .99

num_iteracoes=2000

rList = []
for i in range(num_iteracoes):
    #Reset environment and get first new observation
    s = env.reset()
    rAll = 0
    d = False
    j = 0

    #The Q-Table learning algorithm
    while j < 99:
        j+=1

        #Choose an action by greedily (with noise) picking from Q table
        a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))

        #Get new state and reward from environment
        s1,r,d,_ = env.step(a)

        #Q-Learning Rule
        Q[s,a] = Q[s,a] + alpha*(r + gamma*np.max(Q[s1,:]) - Q[s,a])
        rAll += r
        s = s1
        if d == True:
            break

    #jList.append(j)
    rList.append(rAll)

print("#####################")
print (str(sum(rList)/num_iteracoes))
print("#####################")
print(Q[s,:])
print("#####################")
print("Final Q-Table Values")
print(Q)


