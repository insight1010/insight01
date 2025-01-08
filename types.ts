export type CaseType = 'operational' | 'strategic' | 'hr' | 'market';
export type StageType = 'conflict' | 'ikr' | 'insights';

export interface User {
  id: string;
  name: string;
  avatar: string;
}

export interface Metric {
  key: string;
  value: string;
  icon: string;
}

export interface ConflictPair {
  positive: string;
  negative: string;
  isComplete: boolean;
}

export interface IKR {
  description: string;
  isComplete: boolean;
}

export interface Insight {
  description: string;
  author: User;
  createdAt: Date;
}

export interface Case {
  id: string;
  type: CaseType;
  title: string;
  xElement: {
    problem: string;
    metrics: Metric[];
  };
  stages: {
    current: StageType;
    conflict: ConflictPair | null;
    ikr: IKR | null;
    insights: Insight[];
  };
  participants: {
    author: User;
    members: User[];
    required: number;
  };
  status: {
    createdAt: Date;
    deadline: Date;
    progress: number;
  };
}

export type NotificationType = 
  | 'PARTICIPANTS_READY'
  | 'STAGE_COMPLETE'
  | 'NEW_PROPOSAL'
  | 'STAGE_BLOCKED'
  | 'DEADLINE_APPROACHING'
  | 'CASE_COMPLETE';

export interface Notification {
  id: string;
  type: NotificationType;
  caseId: string;
  message: string;
  createdAt: Date;
  recipients: User[];
} 