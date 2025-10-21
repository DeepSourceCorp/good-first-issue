/**
 * UserProfile type definition
 * Defines the structure for user profile data
 */
export interface UserProfile {
  id: string | number;
  name: string;
  email: string;
  avatar?: string;
  bio?: string;
  createdAt?: Date | string;
  updatedAt?: Date | string;
}

/**
 * Partial UserProfile for updates
 */
export type PartialUserProfile = Partial<UserProfile>;
