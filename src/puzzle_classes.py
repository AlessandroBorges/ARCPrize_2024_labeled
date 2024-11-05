
## This file contains the class labels for the puzzle tasks in the dataset.
## The class labels are based on human classified labels for the puzzle tasks.
class_label_str_list = [
        (0, 'unspecified'), (1, 'extraction'),  (2, 'addition'),  (3, 'alignment'),  (4, 'assemble'),
        (5, 'attraction'),  (6, 'bars'), (7, 'combination'),  (8, 'completion'),  (9, 'connection'),
        (10, 'full fill'),  (11, 'construction'), (12, 'contamination'), (13, 'counting'), (14, 'extension'),
        (15, 'fence'),      (16, 'filling'), (17, 'map order'), (18, 'mapping'), (19, 'match color'),
        (20, 'modification'), (21, 'nesting'), (22, 'pattern'), (23, 'placement'), (24, 'raven'), (25, 'removal'),
        (26, 'replication'),  (27, 'reproduction'), (28, 'rotation'), (29, 'scaling'), 
        (30, 'selection'),  (31, 'sequencing'), (32, 'symmetry'), (33, 'translation'),
    ]

## Task ID and the corresponding human classified class label ID
## The task ID is a unique identifier for a puzzle task.
## The class label ID is the label ID associated with the puzzle type
task_label_id_list = [
        ( "007bbfb7", 29), ( "00d62c1b", 16), ( "017c7c7b", 14), ( "025d127b", 16), ( "045e512c", 26), ( "0520fde7", 15), ( "05269061", 10), ( "05f2a901", 33), ( "06df4c85", 9), ( "08ed6ac7", 16), 
        ( "09629e4f", 24), ( "0962bcdd", 14), ( "0a938d79", 16), ( "0b148d64", 1), ( "0ca9ddb6", 16), ( "0d3d703e", 19), ( "0dfd9992", 8), ( "0e206a2e", 4), ( "10fcaaa3", 14), ( "11852cab", 16),
        ( "1190e5a7", 13), ( "137eaa0f", 4), ( "150deff5", 16), ( "178fcbfb", 6), ( "1a07d186", 4), ( "1b2d62fb", 15), ( "1b60fb0c", 32), ( "1bfc4729", 32), ( "1c786137", 1), ( "1caeab9d", 3),
        ( "1cf80156", 1), ( "1e0a9b12", 4), ( "1e32b0e9", 8), ( "1f0c79e5", 16), ( "1f642eb9", 7), ( "1f85a75f", 1), ( "1f876c06", 9), ( "1fad071e", 13), ( "2013d3e2", 1), ( "2204b7a8", 12),
        ( "22168020", 16), ( "22233c11", 3), ( "2281f1f4", 3), ( "228f6490", 33), ( "22eb0ac0", 6), ( "234bbc79", 4), ( "23581191", 6), ( "239be575", 9), ( "23b5c85d", 1), ( "253bf280", 9),
        ( "25d487eb", 6), ( "25d8a9c8", 22), ( "25ff71a9", 33), ( "264363fd", 4), ( "272f95fa", 22), ( "27a28665", 19), ( "28bf18c6", 26), ( "28e73c20", 11), ( "29623171", 30), ( "29c11459", 9),
        ( "29ec7d0e", 8), ( "2bcee788", 32), ( "2bee17df", 16), ( "2c608aff", 9), ( "2dc579da", 1), ( "2dd70a9a", 9), ( "2dee498d", 1), ( "31aa019c", 1), ( "321b1fc6", 27), ( "32597951", 12),
        ( "3345333e", 32), ( "3428a4f5", 15), ( "3618c87e", 33), ( "3631a71a", 8), ( "363442ee", 27), ( "36d67576", 8), ( "36fdfd69", 12), ( "3906de3d", 16), ( "39a8645d", 1), ( "39e1d7f9", 8),
        ( "3aa6fb7a", 16), ( "3ac3eb23", 26), ( "3af2c5a8", 26), ( "3bd67248", 11), ( "3bdb4ada", 25), ( "3befdf3e", 14), ( "3c9b0459", 28), ( "3de23699", 1), ( "3e980e27", 8), ( "3eda0437", 16),
        ( "3f7978a0", 1), ( "40853293", 9), ( "4093f84a", 5), ( "41e4d17e", 11), ( "4258a5f9", 30), ( "4290ef0e", 3), ( "42a50994", 25), ( "4347f46a", 25), ( "444801d8", 16), ( "445eab21", 19),
        ( "447fd412", 22), ( "44d8ac46", 16), ( "44f52bb0", 19), ( "4522001f", 27), ( "4612dd53", 8), ( "46442a0e", 14), ( "469497ad", 11), ( "46f33fce", 14), ( "47c1f68c", 32), ( "484b58aa", 8),
        ( "48d8fb45", 1), ( "4938f0c2", 32), ( "496994bd", 32), ( "49d1d64f", 32), ( "4be741c5", 19), ( "4c4377d9", 26), ( "4c5c2cf0", 32), ( "50846271", 12), ( "508bd3b6", 11), ( "50cb2852", 21),
        ( "5117e062", 1), ( "5168d44c", 33), ( "539a4f51", 10), ( "53b68214", 14), ( "543a7ed5", 14), ( "54d82841", 3), ( "54d9e175", 19), ( "5521c0d9", 33), ( "5582e5ca", 19), ( "5614dbcf", 25),
        ( "56dc2b01", 33), ( "56ff96f3", 9), ( "57aa92db", 14), ( "5ad4f10b", 1), ( "5bd6f4ac", 1), ( "5c0a986e", 11), ( "5c2c9af4", 11), ( "5daaa586", 1), ( "60b61512", 16), ( "6150a2bd", 28),
        ( "623ea044", 11), ( "62c24649", 32), ( "63613498", 30), ( "6430c8c4", 15), ( "6455b5f5", 30), ( "662c240a", 24), ( "67385a82", 30), ( "673ef223", 9), ( "6773b310", 30), ( "67a3c6ac", 20),
        ( "67a423a3", 30), ( "67e8384a", 32), ( "681b3aeb", 4), ( "6855a6e4", 33), ( "68b16354", 28), ( "694f12f3", 21), ( "6a1e5592", 33), ( "6aa20dc0", 8), ( "6b9890af", 1), ( "6c434453", 20),
        ( "6cdd2623", 9), ( "6cf79266", 30), ( "6d0160f0", 18), ( "6d0aefbc", 27), ( "6d58a25d", 9), ( "6d75e8bb", 16), ( "6e02f1e3", 19), ( "6e19193c", 15), ( "6e82a1ae", 13), ( "6ecd11f4", 19),
        ( "6f8cd79b", 21), ( "6fa7a44f", 32), ( "72322fa7", 7), ( "72ca375d", 1), ( "73251a56", 22), ( "7447852a", 11), ( "7468f01a", 28), ( "746b3537", 19), ( "74dd1130", 28), ( "75b8110e", 4),
        ( "760b3cac", 32), ( "776ffc46", 19), ( "77fdfe62", 19), ( "780d0b14", 19), ( "7837ac64", 18), ( "794b24be", 13), ( "7b6016b9", 19), ( "7b7f7511", 32), ( "7c008303", 27), ( "7ddcd7ec", 15),
        ( "7df24a62", 30), ( "7e0986d6", 1), ( "7f4411dc", 1), ( "7fe24cdd", 28), ( "80af3007", 7), ( "810b9b61", 19), ( "82819916", 12), ( "83302e8f", 19), ( "834ec97d", 11), ( "8403a5d5", 6),
        ( "846bdb03", 23), ( "855e0971", 6), ( "85c4e7cd", 19), ( "868de0fa", 21), ( "8731374e", 11), ( "88a10436", 27), ( "88a62173", 26), ( "890034e9", 23), ( "8a004b2b", 26), ( "8be77c9e", 26),
        ( "8d5021e8", 28), ( "8d510a79", 6), ( "8e1813be", 19), ( "8e5a5113", 28), ( "8eb1be9a", 26), ( "8efcae92", 27), ( "8f2ea7aa", 18), ( "90c28cc7", 19), ( "90f3ed37", 6), ( "913fb3ed", 21),
        ( "91413438", 18), ( "91714a58", 1), ( "9172f3a0", 19), ( "928ad970", 21), ( "93b581b8", 19), ( "941d9a10", 19), ( "94f9d214", 15), ( "952a094c", 23), ( "9565186b", 19), ( "95990924", 19),
        ( "963e52fc", 19), ( "97999447", 22), ( "97a05b5b", 23), ( "98cf29f8", 23), ( "995c5fa3", 17), ( "99b1bc43", 15), ( "99fa7670", 11), ( "9aec4887", 27), ( "9af7a82c", 17), ( "9d9215db", 11),
        ( "9dfd6313", 28), ( "9ecd008a", 8), ( "9edfc990", 2), ( "9f236235", 28), ( "a1570a43", 3), ( "a2fd1cf0", 9), ( "a3325580", 19), ( "a3df8b1e", 15), ( "a416b8f3", 26), ( "a48eeaf7", 5),
        ( "a5313dff", 16), ( "a5f85a15", 19), ( "a61ba2ce", 23), ( "a61f2674", 19), ( "a64e4611", 9), ( "a65b410d", 15), ( "a68b268e", 2), ( "a699fb00", 9), ( "a740d043", 27), ( "a78176bb", 15),
        ( "a79310a0", 23), ( "a85d4709", 19), ( " a87f7484", 27), ( "a8c38be5", 17), ( "a8d7556c", 16), ( "a9f96cdd", 22), ( "aabf363d", 19), ( "aba27056", 15), ( "ac0a08a4", 19), ( "ae3edfdc", 9),
        ( "ae4f1146", 22), ( "aedd82e4", 19), ( "af902bf9", 3), ( "b0c4d837", 13), ( "b190f7f5", 22), ( "b1948b0a", 19), ( "b230c067", 19), ( "b27ca6d3", 30), ( "b2862040", 21), ( "b527c5c6", 14),
        ( "b548a754", 14), ( "b60334d2", 30), ( "b6afb2da", 19), ( "b7249182", 8), ( "b775ac94", 32), ( "b782dc8a", 22), ( "b8825c91", 32), ( "b8cdaf2b", 11), ( "b91ae062", 18), ( "b94a9452", 30),
        ( "b9b7f026", 30), ( "ba26e723", 22), ( "ba97ae07", 16), ( "bb43febb", 21), ( " bbc9ae5d", 15), ( "bc1d5164", 23), ( "bd4472b8", 6), ( "bda2d7a6", 21), ( "bdad9b1f", 11), ( "be94b721", 1),
        ( "beb8660c", 15), ( "c0f76784", 21), ( "c1d99e64", 11), ( "c3e719e8", 7), ( "c3f564a4", 10), ( "c3f564a4", 27), ( "c59eb873", 27), ( "c8cbb738", 23), ( "c8f0f002", 19), ( "c909285e", 26),
        ( "c9e6f938", 28), ( "c9f8e694", 19), ( "caa06a1f", 22), ( "cbded52d", 6), ( "cce03e0d", 11), ( "cdecee7f", 13), ( "ce22a75a", 11), ( "ce4f8723", 2), ( "ce602527", 27), ( "ce9e57f2", 6),
        ( "cf98881b", 2), ( "d037b0a7", 6), ( "d06dbe63", 15), ( "d07ae81c", 15), ( "d0f5fe59", 15), ( "d10ecb37", 26), ( "d13f3404", 15), ( "d22278a0", 21), ( "d23f8c26", 1), ( "d2abd087", 19),
        ( "d364b489", 11), ( "d406998b", 7), ( "d43fd935", 9), ( "d4469b4b", 19), ( "d4a91cb9", 9), ( "d4f3cd78", 14), ( "d511f180", 19), ( "d5d6de2d", 16), ( "d631b094", 13), ( "d687bc17", 5),
        ( "d6ad076f", 9), ( "d89b689b", 4), ( "d8c310e9", 22), ( "d90796e8", 25), ( "d9f24cd1", 6), ( "d9fac9be", 30), ( "dae9d2b5", 2), ( "db3e9e38", 15), ( "db93a21d", 11), ( "dbc1a6ce", 9),
        ( "dc0a314f", 8), ( "dc1df850", 21), ( "dc433765", 23), ( "ddf7fa4f", 19), ( "de1cd16c", 30), ( "ded97339", 9), ( "e179c5f4", 15), ( "e21d9049", 7), ( "e26a3af2", 1), ( "e3497940", 2),
        ( "e40b9e2f", 32), ( "e48d4e1a", 23), ( "e5062a87", 23), ( "e509e548", 19), ( "e50d258f", 26), ( "e6721834", 23), ( "e73095fd", 16), ( "e76a88a6", 22), ( "e8593010", 16), ( "e8dc4411", 15),
        ( "e9614598", 11), ( "e98196ab", 2), ( "e9afcf9a", 7), ( "ea32f347", 13), ( " ea786f4a", 15), ( "eb281b96", 32), ( "eb5a1d5d", 23), ( "ec883f72", 15), ( "ecdecbb3", 9), ( "ed36ccf7", 28),
        ( "ef135b50", 9), ( "f15e1fac", 6), ( "f1cefba8", 11), ( "f25fbde4", 27), ( "f25ffba3", 32), ( "f2829549", 1), ( "f35d900a", 21), ( "f5b8619d", 27), ( "f76d97a5", 26), ( "f8a8fe49", 28),
        ( "f8b3ba0a", 13), ( "f8c80d96", 11), ( "f8ff0b80", 17), ( "f9012d9b", 22), ( "fafffa47", 1), ( "fcb5c309", 26), ( "fcc82909", 11), ( "feca6190", 15), ( "ff28f65a", 7), ( "ff805c23", 22),           
]

print("Len Puzzle Classes: ", len(class_label_str_list))
print("Len Tasks: ", len(task_label_id_list))

dict_class_label_str = {}
dict_task_label_id = {}

# Create a dictionary with the class label string
for class_label in class_label_str_list:
    dict_class_label_str[class_label[0]] = class_label[1]

# a global variable to keep track of unknown tasks
outlier_ord = 500

 
def get_labels():
    """
    Get the list of class labels.

    Returns:
        list: A list of tuples containing:
            - int: The label ID
            - str: The human-readable label string
    """
    return class_label_str_list

def get_tasks_by_label(label_id)->list:
    """
    Get the list of tasks with a specific label.
    Args:
        label_id (int): The label ID to filter tasks by.
    Returns:
        list: A list of task IDs that have the specified label.
    """
    task_list = []
    for task in task_label_id_list:
        if task[1] == label_id:
            task_list.append(task[0])
    return task_list

def get_task_metadata(task_id):
    """
    Get puzzle metadata from a task ID.

    Args:
        task_id (str): The unique identifier for a puzzle task.

    Returns:
        tuple: A tuple containing:
            - int: The puzzle's order number in the sequence
            - int: The label ID associated with the puzzle type
            - str: The human-readable label string describing the puzzle type

    Note:
        If the task_id is not found, returns (outlier_ord, 0, 'unspecified')
        where outlier_ord is an incrementing counter for unknown tasks.
    """
    global outlier_ord  # declare outlier_ord as global
    task_id = task_id.lower()
    ord = 0
    for task in task_label_id_list:
        ord +=1
        if task[0] == task_id:
            label_id = task[1]
            label_str = dict_class_label_str[label_id]
            return ord, label_id, label_str
        
    print("*** Task ID not found: ", task_id)    
    outlier_ord += 1
    label_str = dict_class_label_str[0]  
    
    # if not found, return the outlier order, label_id = 0 and label_str = 'unspecified'      
    return outlier_ord, 0, label_str

#print(get_task_label_id("ff805c23"))
#print(get_task_label_id("007bbfb7"))
if __name__ == "__main__":
    print("puzzle_classes.py")  

        
    print("Puzzle #ff805c23 - ", get_task_metadata("ff805c23"))
    print("Puzzle #007bbfb7 - ", get_task_metadata("007bbfb7"))
    print("Puzzle #00000000 - ",get_task_metadata("00000000"))