def solution(video_len, pos, op_start, op_end, commands):
    total_video_len = calc_total_video_len(video_len)
    pos_by_second = calc_total_video_len(pos)
    op_start_by_second = calc_op_start(op_start)
    op_end_by_second = calc_op_end(op_end)
    
    if((pos_by_second >= op_start_by_second) and (pos_by_second <= op_end_by_second)):
            pos_by_second = op_end_by_second
    for command in commands:  
        if(command == "prev"):
            pos_by_second -= 10
        else:
             pos_by_second += 10

        if(total_video_len < pos_by_second):
            pos_by_second = total_video_len
        elif(pos_by_second < 0):
            pos_by_second = 0
        if((pos_by_second >= op_start_by_second) and (pos_by_second <= op_end_by_second)):
            pos_by_second = op_end_by_second
            
    answer = ''
    if(pos_by_second // 60 < 10):
        answer = "0" + str(pos_by_second//60) + ":"
    else:
        answer = str(pos_by_second//60) + ":"

    if(pos_by_second % 60 < 10):
        answer += ("0"+str(pos_by_second%60))
    else:
        answer += str(pos_by_second%60)
        
    return answer

def calc_total_video_len(video_len):
    video_len_minute, video_len_second = video_len.split(":")
    video_len_by_second = int(video_len_minute) * 60 + int(video_len_second)
    return video_len_by_second

def calc_pos(pos):
    pos_minute, pos_second = pos.split(":")
    pos_by_second = int(pos_minute) * 60 + int(pos_second)
    return pos_by_second

def calc_op_start(op_start):
    op_start_minute, op_start_second = op_start.split(":")
    op_start_by_second = int(op_start_minute) * 60 + int(op_start_second)
    return op_start_by_second

def calc_op_end(op_end):
    op_end_minute, op_end_second = op_end.split(":")
    op_end_by_second = int(op_end_minute) * 60 + int(op_end_second)
    return op_end_by_second