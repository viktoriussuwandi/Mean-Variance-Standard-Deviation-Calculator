import numpy as np

def calculate(list):
  if len(list) < 9 : raise ValueError('List must contain nine numbers.')
  else :
    arr     = np.array(list)
    matrix  = arr.reshape(3,3)
    
    calculation = {
      'mean'     : calc_mean(matrix),
      'variance' : calc_var(matrix),
      'standard deviation' : calc_std_dev(matrix),
      'max'      : calc_max(matrix),
      'min'      : calc_min(matrix),
      'sum'      : calc_sum(matrix)
    }
    
    return calculation
    
def calc_mean(matrix) :
  axis1    = np.mean(matrix,axis=0)
  axis2    = np.mean(matrix,axis=1)  
  mean_val = np.mean(matrix)
  res      = [ axis1.tolist(), axis2.tolist(), mean_val]
  return res

def calc_var(matrix) :
  axis1   = np.var(matrix,axis=0)
  axis2   = np.var(matrix,axis=1)
  var_val = np.var(matrix)
  res      = [ axis1.tolist(), axis2.tolist(), var_val]
  return res

def calc_std_dev(matrix) :
  axis1   = np.std(matrix,axis=0)
  axis2   = np.std(matrix,axis=1)  
  std_val = np.std(matrix)
  res      = [ axis1.tolist(), axis2.tolist(), std_val]
  return res

def calc_max(matrix) :
  axis1   = np.max(matrix,axis=0)
  axis2   = np.max(matrix,axis=1)  
  max_val = np.max(matrix)
  res      = [ axis1.tolist(), axis2.tolist(), max_val]
  return res

def calc_min(matrix) :
  axis1   = np.min(matrix,axis=0)
  axis2   = np.min(matrix,axis=1)  
  min_val = np.min(matrix)
  res      = [ axis1.tolist(), axis2.tolist(), min_val]
  return res

def calc_sum(matrix) :
  axis1   = np.sum(matrix,axis=0)
  axis2   = np.sum(matrix,axis=1)  
  sum_val = np.sum(matrix)
  res      = [ axis1.tolist(), axis2.tolist(), sum_val]
  return res