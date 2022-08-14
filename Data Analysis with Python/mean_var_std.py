import numpy as np

# the input will be a list of 9 digits
def calculate(list):
  #try run the function
  try:
      #convert from list to 3x3 numpy array
    A = np.array(list).reshape(3,3)
    calculations = {'mean':[[A[:,0].mean(), A[:,1].mean(), A[:,2].mean()],[A[0,:].mean(), A[1,:].mean(), A[2,:].mean()],np.mean(A)],'variance': [[np.var(A[:,0]), np.var(A[:,1]), np.var(A[:,2])],[np.var(A[0,:]), np.var(A[1,:]), np.var(A[2,:])],np.var(A)],'standard deviation': [[np.std(A[:, 0]), np.std(A[:, 1]), np.std(A[:, 2])],[np.std(A[0, :]), np.std(A[1, :]), np.std(A[2, :])], np.std(A)],'max': [[np.max(A[:, 0]), np.max(A[:, 1]), np.max(A[:, 2])],[np.max(A[0, :]), np.max(A[1, :]), np.max(A[2, :])], np.max(A)],'min': [[np.min(A[:, 0]), np.min(A[:, 1]), np.min(A[:, 2])],[np.min(A[0, :]), np.min(A[1, :]), np.min(A[2, :])], np.min(A)],'sum': [[np.sum(A[:, 0]), np.sum(A[:, 1]), np.sum(A[:, 2])],[np.sum(A[0, :]), np.sum(A[1, :]), np.sum(A[2, :])], np.sum(A)]}
    return calculations
  #if the number are not nine or there is any other error print "List must contain nine numbers."
  except:
    raise ValueError('List must contain nine numbers.')

if __name__ == '__main__':
  calculate([2,6,2,8,4,0,1,])