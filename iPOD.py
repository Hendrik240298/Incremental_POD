def iPOD(
    POD,  # POD basis
    snapshot,  # new snapshot to be added to POD basis
    bunch_matrix,  # bunch matrix
    bunch_size,  # desired size of bunch matrix
    singular_values,  # singular values of POD basis
    total_energy,  # total energy of POD basis
    energy_content,  # desired energy content
):

    if bunch_matrix.shape[1] == 0:
        # initialize bunch matrix if empty
        bunch_matrix = snapshot  # np.empty([np.shape(snapshot)[0], 0])
    else:
        # concatenate new snapshot to bunch matrix
        bunch_matrix = np.hstack((bunch_matrix, snapshot.reshape(-1, 1)))

    # add energy of new snapshot to total energy
    total_energy += np.dot((snapshot), (snapshot))

    # check bunch_matrix size to decide if to update POD
    if bunch_matrix.shape[1] == bunch_size:
        # initialize POD with first bunch matrix
        if POD.shape[1] == 0:
            POD, S, _ = scipy.linalg.svd(bunch_matrix, full_matrices=False)

            # compute the number of POD modes to be kept
            r = 0
            while (np.dot(S[0:r], S[0:r]) / total_energy <= energy_content) and (
                r <= np.shape(S)[0]
            ):
                r += 1

            singular_values = S[0:r]
            POD = POD[:, 0:r]
        # update POD with  bunch matrix
        else:
            M = np.dot(POD.T, bunch_matrix)
            P = bunch - np.dot(POD, M)

            Q_p, R_p = scipy.linalg.qr(P, mode="economic")
            Q_q = np.hstack((POD, Q_p))

            S0 = np.vstack(
                (
                    np.diag(singular_values),
                    np.zeros((np.shape(R_p)[0], np.shape(singular_values)[0])),
                )
            )
            MR_p = np.vstack((M, R_p))
            K = np.hstack((S0, MR_p))

            # check the orthogonality of Q_q heuristically
            if np.inner(Q_q[:, 0], Q_q[:, -1]) >= 1e-10:
                Q_q, R_q = scipy.linalg.qr(Q_q, mode="economic")
                K = np.matmul(R_q, K)

            # inner SVD of K
            U_k, S_k, _ = scipy.linalg.svd(K, full_matrices=False)

            # compute the number of POD modes to be kept
            r = 0 
            while (np.dot(S_k[0:r], S_k[0:r]) / total_energy <= energy_content) and (
                r < np.shape(S_k)[0]
            ):
                r += 1

            singular_values = S_k[0:r]
            POD = np.matmul(Q_q, U_k[:, 0:r])

        # empty bunch matrix after update
        bunch_matrix = np.empty([np.shape(bunch_matrix)[0], 0])

    return POD, bunch_matrix, singular_values, total_energy
